# Using @classmethods

In Python, a class method is a method that is bound to the class and not the instance of the object. It is defined using the `@classmethod` decorator, and it takes the `class` as its first argument, rather than `self`. Class methods are typically used as alternative constructors for a class, but can be used for other purposes as well.

## Example 1

```python
class Points():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    @classmethod
    def from_tuple(cls, coords):
        x,y = coords
        return cls(x,y)
    
    @classmethod
    def from_dictionary(cls, coord_dict):
        x = coord_dict["x"]
        y = coord_dict["y"]
        return cls(x,y)
    
point1 = Points.from_tuple((1,2))
point2 = Points.from_dictionary({"x" : 3, "y" : 4})

print(point1.x, point1.y)
print(point2.x, point2.y)
```

In this example, the `Point` class has two class methods, `from_tuple` and `from_dict`, which are alternative constructors for the class. These methods take different inputs (a tuple and a dictionary, respectively) and use them to create and return instances of the `Point` class. This allows the user to create `Point` object in multiple ways, which makes the code more flexible.

## Example 2

```python
class MyMath:
    pi = 3.14
    
    @classmethod
    def add_pi(cls, number):
        return number + cls.pi
    
    @classmethod
    def get_pi(cls):
        return cls.pi
   
print(MyMath.get_pi()) 
print(MyMath.add_pi(5))
```

In this example, `add_pi` is a class method that takes a number as an argument and returns the result of adding that number to the class variable `pi`. This method can be used as a utility function for any instance of the class and it does not need to have an instance of the class to access it.

You can also use class method to access class level variables and methods on the class level.
