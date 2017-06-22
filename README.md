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

# 5. Relationships & Hyperlinked APIs
http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
- Create an endpoint for root of API
- Create an endpoint for highlighted snippets
- Hyperlink API so things are more easily clickable and browsable
- Name the URL patterns so it's easier to reference URLs from fields:
    * The root of our API refers to 'user-list' and 'snippet-list'.
    * Our snippet serializer includes a field that refers to 'snippet-highlight'.
    * Our user serializer includes a field that refers to 'snippet-detail'.
    * Our snippet and user serializers include 'url' fields that by default will refer to '{model_name}-detail', which in this case will be 'snippet-detail' and 'user-detail'.
- Add pagination    
    
# 6. ViewSets and Routers
http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
- Create ViewSets from existing views
- Create a Router that binds all of the ViewSets and automatically creates all URLs
- ViewSets are less explicit but are quicker to develop, and maintain.     

# 7. Schemas & client libraries
http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/

# 8. Django REST Swagger
https://github.com/marcgibbons/django-rest-swagger

# 9. Django HTML Forms with a Serializer
- http://www.django-rest-framework.org/topics/html-and-forms/
- http://www.django-rest-framework.org/api-guide/fields/

## Last Words:
Contribute on GitHub by reviewing and submitting issues, and making pull requests. (https://github.com/encode/django-rest-framework)
Join the REST framework discussion group, and help build the community. (https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework)
Follow the author on Twitter and say hi. (https://twitter.com/_tomchristie)