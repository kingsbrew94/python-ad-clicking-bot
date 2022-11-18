<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {~ usecss('libs/semantic-ui/semantic.min') ~}
    {~ usecss('libs/font-awesome/css/font-awesome.min') ~}
    @usecss('style')

    <title>{~ $app_name ~}</title>
</head>
<body>
    <!-- ${~ echo '<h1> Hello Fly </h1>' ~} -->
    
    {:children}
    {~ usejs('libs/semantic-ui/semantic.min') ~}
    @usejs('libs/brew/lib',['data-main' => statics('js/src',false)])
</body>
</html>