<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
      

        body {
          background: #C5E1A5;
        }
        form {
          width: 60%;
          margin: 60px auto;
          background: #efefef;
          padding: 60px 120px 80px 120px;
          text-align: center;
          -webkit-box-shadow: 2px 2px 3px rgba(0,0,0,0.1);
          box-shadow: 2px 2px 3px rgba(0,0,0,0.1);
          border-radius: 3px;
        }
        label {
          display: block;
          position: relative;
          margin: 40px 0px;
        }
        
        .input {
          width: 100%;
          padding: 10px;
          background: transparent;
          border: none;
          outline: none;
        }

        button {
          display: inline-block;
          padding: 12px 24px;
          background: rgb(220,220,220);
          font-weight: bold;
          color: rgb(120,120,120);
          border: none;
          outline: none;
          border-radius: 3px;
          cursor: pointer;
          transition: ease .3s;
        }

        button:hover {
          background: #8BC34A;
          color: #ffffff;
        }
        .DMK {
        position: relative;
        display: inline-block;
        padding: 12px 24px;
        background: #ccc;
        font-weight: bold;
        color: rgb(red, green, blue);
        border: none;
        outline: none;
        border-radius: 3px;
        cursor: pointer;
        font-size: large;
        bottom: -50px;
        left: 1700px
    }
</style>
<body>
<a class="DMK" href="TK.php">Back</a>
<form action="UpdateEmail.php" method="GET">
        <label for="new-email">New Email:</label>
        <input type="email" id="new-email" name="new-email" required />
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required />
        <input type="submit" value="Change Email" />
    </form>
</body>
</html>
