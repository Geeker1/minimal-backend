import graphene
import django_filters
from graphene_django.types import DjangoObjectType, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Product, Category

class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            'category':['exact'],
            'category__name':['exact', 'icontains', 'istartswith'],
            'name':['exact', 'icontains', 'istartswith']
        }
        interfaces = (graphene.relay.Node,)

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name','slug','id']
        interfaces = (graphene.relay.Node,)


class ProductInput(graphene.InputObjectType):
    category = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    short_description = graphene.String()
    price = graphene.Float()
    available = graphene.Boolean()
    stock = graphene.Int()
    image = graphene.String()
    slug = graphene.String()

class RelayCreateProduct(graphene.relay.ClientIDMutation):
    product = graphene.Field(ProductNode)

    class Input:
        product = ProductInput(required=True)

    @classmethod
    def mutate_and_get_payload(cls,root, info, product):

        category = Category.objects.get(id=product.category)

        product = Product(
            name=product.name,
            category=category, description=product.description,
            short_description=product.short_description, price=product.price,
            available=product.available, stock=product.stock,
            image=product.image, slug=product.slug)
        product.save()

        return cls(product=product)


class Mutation(ObjectType):
    create_product = RelayCreateProduct.Field()

class Query(ObjectType):
    product = graphene.relay.Node.Field(ProductNode)
    category = graphene.relay.Node.Field(CategoryNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
