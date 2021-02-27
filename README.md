## image-rep

#### This app can be used to upload your images, get the list of endpoint of image address and also delete the images using the below API's.

#### cURL to upload the images
`curl --location --request POST 'https://imagerep.herokuapp.com/images/' \
--form 'image=@"ex.jpeg"' \
--form 'title="new"'`

#### cURL to get the list of images in sorted order with recent one on top
`curl --location --request GET 'https://imagerep.herokuapp.com/images/'`

#### cURL to get the image with title
`curl --location --request GET 'https://imagerep.herokuapp.com/images/?title=new'`

#### cURL to delete the image
`curl --location --request DELETE 'https://imagerep.herokuapp.com/images/9/'`
