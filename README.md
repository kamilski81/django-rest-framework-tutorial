# 1. Serialization
http://www.django-rest-framework.org/tutorial/1-serialization/
- Setup an environment
- Add Project tutorial
- Add App snippets
- Create models
- Add rest_framework to settings.py
- Create models
- Create migrations
- Create serializers using serializers.Serializer
- Learn how to work with Serializers
- Work with views and write native Django code for JSON serialization and deserialization

# 2. Requests and Responses
http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
- Introduce REST Request, Response, Status objects
- Introduce wrappers for @api_view function based views and APIView for class-based views
- Added format types (ie. json and html)
- Introduced Browsability API (http://www.django-rest-framework.org/topics/browsable-api/)

# 3. Class-based Views
http://www.django-rest-framework.org/tutorial/3-class-based-views/
- Use Class-based views (ie. APIView) 

# 4. Authentication and Permissions
http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
- Associate the Snippet model with a User (owner)
- Serialize the Snippet with a ForeignKey User b/c you have to be explicit with relationships
- Add permissions so that you have to be logged in to Create a Snippet
- Add permissions so that only the owner can update/delete a Snippet (object permissions)
- Read more about Authentication if necessary: http://www.django-rest-framework.org/api-guide/authentication/
