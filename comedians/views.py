from django.shortcuts import render
from comedians.models import Comedian
from django.shortcuts import get_object_or_404
from polls.models import Poll
from django.db.models import Count, Q


def index(request, *args, **kwargs):
    comedians = Comedian.objects.all()
    context = {'comedians': comedians}
    return render(request, 'comedians/index.html', context)

def detail(request, *args, **kwargs):
    comedian = get_object_or_404(Comedian, pk=kwargs['comedian_id'])
    context = {'comedian': comedian}
    return render(request, 'comedians/detail.html', context)

def result(request, *args, **kwargs):
    comedian = get_object_or_404(Comedian, pk=kwargs['comedian_id'])
    result = request.GET.get('result')
    user_agent = request.META['HTTP_USER_AGENT']

    # IP取得
    forwarded_addresses = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_addresses:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがある場合: 転送経路の先頭要素を取得する。
        client_addr = forwarded_addresses.split(',')[0]
    else:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがない場合: 直接接続なので'REMOTE_ADDR'ヘッダを参照する。
        client_addr = request.META.get('REMOTE_ADDR')
    
    # IPの後ろから４桁削除(ex: 123.456.789.012 → 123.456.78, 123.456.78.012 → 123.456.78)
    splited_ip = client_addr.split('.')[:-1]
    if len(splited_ip[2]) == 3:
        splited_ip[2] = splited_ip[2][:-1]
    modified_ip = f'{splited_ip[0]}.{splited_ip[1]}.{splited_ip[2]}'

    if not Poll.objects.filter(comedian=comedian, user_agent=user_agent, ip_address=modified_ip).exists():
        if result == 'pro':
            Poll.objects.create(comedian=comedian, user_agent=user_agent, ip_address=modified_ip, is_funny=True)
        else:
            Poll.objects.create(comedian=comedian, user_agent=user_agent, ip_address=modified_ip, is_funny=False)
    
    poll = Poll.objects.filter(comedian=comedian).aggregate(
        pro_count=Count('pk', filter=Q(is_funny=True)),
        con_count=Count('pk', filter=Q(is_funny=False)),
    )
    context = {
        'comedian': comedian,
        'result': result,
        'pro_count': poll['pro_count'],
        'con_count': poll['con_count'],
    }
    return render(request, 'comedians/result.html', context)