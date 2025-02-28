from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid= models.UUIDField(default=uuid.uuid4, editable=False, primary_key= True)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug= models.SlugField(unique=True)
    product_description= models.TextField()
    product_price= models.FloatField(default=0.0)
    
    
class ProductMetaInfo(BaseModel):
    product= models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta info" )
    quantity= models.CharField(null=True, blank= True)
    product_unit= models.CharField(max_length=100, choices=(("kg", "kg"), ("ml", "ml"), ("L","L"), ("pcs","pcs")))
    restrict= models.IntegerField()
    is_restrict= models.BinaryField(default=False)

class ProductImages(BaseModel):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_img= models.ImageField(upload_to= "products")
