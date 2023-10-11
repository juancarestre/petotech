### retrieve a object from dynamodb with id 1
 aws dynamodb get-item --table-name pokemon --key '{"id":{"S":"1"}}' --profile juan