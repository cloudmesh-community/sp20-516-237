import textwrap


class GenerateOpenAPI:

    openAPITemplate = """
openapi: 3.0.0
info:
  title: {title}
  description: {description}
  version: "{version}"
servers:
  - url: http://localhost/cloudmesh/{title}
    description: Optional server description, e.g. Main (production) server
paths:
  /{name}:
     get:
      summary: {description}
      description: Optional extended description in CommonMark or HTML.
      operationId: {name}
      responses:
        '200':    # status code
          description: {description}
          content:
            text/plain:
              schema: 
                type: {return_type}
      parameters:
         {parameters} 
      
  /users:
    get:
      summary: Returns a list of users.
      description: Optional extended description in CommonMark or HTML.
      responses:
        '200':    # status code
          description: A JSON array of user names
          content:
            application/json:
              schema: 
                type: array
                items: 
                  type: string
"""

    def generate_parameter(self, name, _type, description):
        spec = textwrap.dedent(f"""
            - in: query
              name: {name}
              schema:
                type: {_type}
              description: {description}
        """)
        return spec

    def generate_openapi(self, f, write=True):
        description = f.__doc__.strip().split("\n")[0]
        version = "1.0"  # hard coded for now
        title = f.__name__
        return_type = str()
        parameters = str()
        for parameter, _type in f.__annotations__.items():

            # print(parameter, _type)
            if _type == int:
                _type = 'integer'
            elif _type == bool:
                _type = 'boolean'
            elif _type == float:
                _type = 'number'   # used number because per swagger validator float is not supported
            else:
                _type = 'unkown'

            if parameter == "return":
                return_type = _type
            else:
                parameters += self.generate_parameter(parameter, _type, "not yet available, you can read it from docstring")

        parameters = textwrap.indent(parameters, ' ' * 9)

        spec = self.openAPITemplate.format(
            title=title,
            name=f.__name__,
            description=description,
            version=version,
            return_type=return_type,
            parameters=parameters.strip()
        )

        if write:
            version = open(f"{title}.yaml", 'w').write(spec)

        return spec



