from django.db import models


class Comedian(models.Model):
    name = models.CharField(max_length=128, verbose_name='芸名')
    group = models.ForeignKey('comedians.Group', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='グループ')
    is_solo = models.BooleanField(default=False, verbose_name='ピン芸人')
    company = models.ForeignKey('comedians.Company', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='会社')
    tags = models.ManyToManyField('comedians.Tag',
                                    blank=True,
                                    related_name='comedian_tags',
                                    through='comedians.ComedianTagGroup',
                                    verbose_name='タグ一覧')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新日')

    class Meta:
        verbose_name = '芸人（個人）'
        verbose_name_plural = '芸人（個人）'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128, verbose_name='グループ名')
    tags = models.ManyToManyField('comedians.Tag',
                                         blank=True,
                                         related_name='group_tags',
                                         through='comedians.GroupTagGroup',
                                         verbose_name='タグ一覧')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新日')

    class Meta:
        verbose_name = 'グループ'
        verbose_name_plural = 'グループ'
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='タグ名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新日')

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'
    
    def __str__(self):
        return self.name


class ComedianTagGroup(models.Model):
    comedian = models.ForeignKey('comedians.Comedian',
                              on_delete=models.CASCADE,
                              related_name='+',
                              verbose_name='芸人')
    tag = models.ForeignKey('comedians.Tag',
                            on_delete=models.CASCADE,
                            related_name='+',
                            verbose_name='タグ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')

    class Meta:
        unique_together = ('comedian', 'tag')
        verbose_name = '芸人のタグ紐付け'
        verbose_name_plural = '芸人のタグ紐付け'


class GroupTagGroup(models.Model):
    group = models.ForeignKey('comedians.Group',
                              on_delete=models.CASCADE,
                              related_name='+',
                              verbose_name='グループ')
    tag = models.ForeignKey('comedians.Tag',
                            on_delete=models.CASCADE,
                            related_name='+',
                            verbose_name='タグ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')

    class Meta:
        unique_together = ('group', 'tag')
        verbose_name = 'グループのタグ紐付け'
        verbose_name_plural = 'グループのタグ紐付け'


class Company(models.Model):
    name = models.CharField(max_length=256, verbose_name='会社名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新日')

    class Meta:
        verbose_name = '会社'
        verbose_name_plural = '会社'
    
    def __str__(self):
        return self.name