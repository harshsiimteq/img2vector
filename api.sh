curl -X 'POST' 'http://localhost:8000/convert-image-to-vector' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@test_image.jpg'
