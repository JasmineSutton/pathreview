from api.main import app
import json

schema = app.openapi()
for path in ['/profiles', '/reviews']:
    print('PATH', path)
    print(json.dumps(schema['paths'][path]['post'], indent=2))
    print('---')
