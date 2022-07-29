# Applied Database Technologies Final Project
## Usage
The application can be found here: https://test-django-sfields.herokuapp.com/

### RESTQL
An example of a url utilizing the restql functionality is as such: `https://test-django-sfields.herokuapp.com/physician/?query={First_Name,%20Gender}`

### Django Filters
An example of the filters is as follow: `https://test-django-sfields.herokuapp.com/physician/?NPI=&Last_Name_Or_Org=&First_Name=&MI=&Credentials=&Gender=F&Entity_Type=&Physician_Type=&MPI=`

Note that the filters match exactly currently, with no ability for a "like" match on strings or LT and GT features for numbers. This isn't a shortcoming of the package but rather left out in the implementation of this mock.

### A combination of both:
For some reason the query for the restql framework needs to come before the filters. Here is an example combining the two: `https://test-django-sfields.herokuapp.com/physician/?query={First_Name,%20Gender}&?NPI=&Last_Name_Or_Org=&First_Name=&MI=&Credentials=&Gender=F&Entity_Type=&Physician_Type=&MPI=`