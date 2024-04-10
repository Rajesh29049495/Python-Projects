import abc

class MedicalDocParser(metaclass = abc.ABCMeta):             # this class will take text that we got from the tesseract,,,,This is the abstract base class,,,,,,,,use the `abc` module to create abstract base classes by subclassing `ABC` or `ABCMeta`. Abstract base classes cannot be instantiated directly and typically include one or more abstract methods that must be implemented by subclasses.
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod               # this is method to decorate a method as an abstract method,which means when i will be in this abstract base class's subclass like `PrescriptionParser` and if i don't write the `parse` method in that then will not able to run that class. This is the way this abstrcat base class enforce all teh child classes/subclasses to have certain method mandaterally. Here in my project there are only two subclasses,but in bigger projects there may be more of them, so by using this we can ensure certain methods implementaion in them for sure, to make those subclasses follow a certain set framework in there making
    def parse(self):                   # this method will return json dictionary where we will have all the information that we want to extract from the text we got from tesseract   But since this a generic parser, we leave this method empty
        pass

