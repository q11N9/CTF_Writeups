<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chat</title>
  <style>
    .navigation-header2 {
      position: relative;
      display: inline-block;
      padding: 12px 24px;
      background: rgb(240, 189, 242);
      font-weight: bold;
      color: rgb(red, green, blue);
      border: none;
      outline: none;
      border-radius: 3px;
      cursor: pointer;
      font-size: large;
      position: relative;
      left: 1650px;
      top: 100px;
    }
  </style>
</head>

<body>
  <?php
  $servername = "localhost";
  $userN = "root";
  $passW = "";
  $dbname = "webbanhang";
  $conn = new mysqli($servername, $userN, $passW, $dbname);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  session_start();
  $username = $_SESSION['username'];
  $sql = "SELECT UserName FROM user";
  $result = $conn->query($sql);
  echo '<a class="navigation-header2" href=../login/sanpham.php>Back</a>';
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $name = $row['UserName'];
      if (strtolower($name) != strtolower($username)) {
        echo "<li><strong>$name:</strong><form method='POST' action='chat1.php?name1=$name'><input type='hidden' name='name1' value='$name'><button type='submit'>Chat</button></form></li>";
      }
    }
  } else {
    echo "Không có bình luận nào.";
  }

  ?>
</body>

</html>