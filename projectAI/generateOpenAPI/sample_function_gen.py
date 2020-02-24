import sys
sys.path.append('/Users/Jonathan/cm/sp20-516-237/projectAI/generateOpenAPI/')
import generateOpenAPI as gen

def sampleFunction(x: int, y: float) -> float:
    """
    Multiply int and float sample.
    :param x: x value
    :type x: int
    :param y: y value
    :type y: float
    :return: result
    :return type: float
    """
    return x * y

f = sampleFunction
openAPI = gen.GenerateOpenAPI()
spec = gen.GenerateOpenAPI.generate_openapi(openAPI, f)
print(spec)

