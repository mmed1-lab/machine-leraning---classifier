
from models.Product import Product
from models.Comment import Comment
from service.predection_service import sentimentPrediction


class ProductService:

    def __init__(self):

        self.products = [
            Product(
                name="Laptop HP",
                price=7500,
                comments=[
                    self.createComment("Excellent product!"),
                    self.createComment("Battery is average.")
                ]
            ),
            Product(
                name="iPhone 15",
                price=9000,
                comments=[
                    self.createComment("Amazing camera!"),
                    self.createComment("Too expensive.")
                ]
            ),
            Product(
                name="Samsung TV",
                price=5500,
                comments=[
                    self.createComment("Great image quality.")
                ]
            ),
            Product(
                name="Logitech Mouse",
                price=250,
                comments=[
                    self.createComment("Good value for money.")
                ]
            ),
            Product(
                name="Dell Monitor",
                price=2200,
                comments=[
                    self.createComment("Average display.")
                ]
            )
        ]

    # Predict sentiment and create a comment
    def createComment(self, message: str):

        prediction = sentimentPrediction.predictSentiment(message)

        return Comment(
            message=message,
            label=prediction["sentiment"]
        )

    # Insert a new product
    def addProduct(self, product: Product):
        self.products.append(product)
        return product

    # Select all products
    def getProducts(self):
        return self.products

    # Select comments of a specific product
    def selectCommentProduct(self, prodId):
        for product in self.products:
            if str(product.id) == str(prodId):
                return product.comments

        raise Exception(f'No product with id: {prodId}')
    
    
    def addCommentProduct(self, prodId: str, message: str):

        for product in self.products:
            if str(product.id) == str(prodId):

                prediction = sentimentPrediction.predictSentiment(message)

                comment = Comment(
                    message=message,
                    label=prediction['sentiment']
                )

                product.comments.append(comment)

                return comment

        raise Exception(f'No product with id: {prodId}')

