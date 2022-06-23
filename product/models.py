from django.db import models


STATUS_COHICE = (
    ("판매중","판매중"),
    ("판매종료","판매종료")
)
    


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    name = models.CharField("상품명", max_length=50)
    image = models.FileField("썸네일", upload_to='productimg')
    dec = models.TextField("상품설명")
    registered_date = models.DateField("등록일", auto_now_add=True)
    updated_date = models.DateField("등록일", auto_now=True)
    start_date = models.DateField("노출 시작일", null=True, blank=True) 
    end_date = models.DateField("노출 종료일", null=True, blank=True)
    status = models.CharField("활성화 여부", choices=STATUS_COHICE, max_length=30)
    
    def __str__(self):
        return f"{self.name} / {self.user.username} / "
    
    
class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    contents = models.TextField("리뷰")
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateField("작성일", auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} / {self.user}" 