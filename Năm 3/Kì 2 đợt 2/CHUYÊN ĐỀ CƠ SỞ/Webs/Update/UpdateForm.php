<!doctype html>
<html lang="en">
  <head>
    <title>REGISTER</title>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

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
  </head>
  <body>
  <a class="DMK" href="TK.php">Back</a>
  <form action="UpdateSubmit.php" method="post">
    <label for="old_password">Mật khẩu cũ:</label>
    <input type="password" name="old_password" id="old_password" required>
   
    <label for="new_password">Mật khẩu mới:</label>
    <input type="password" name="new_password" id="new_password" required>
    
    <label for="confirm_password">Xác nhận mật khẩu mới:</label>
    <input type="password" name="confirm_password" id="confirm_password" required>
    <br> </br>
    <button type="submit" name="submit">Đổi mật khẩu</button>
    </form>

  </body>

</html>