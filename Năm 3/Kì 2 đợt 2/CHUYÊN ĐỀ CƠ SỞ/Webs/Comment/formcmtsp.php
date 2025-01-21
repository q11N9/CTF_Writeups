<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<style>
    .formPostCMT {
        position: relative;
        bottom: 200px;
        left: 700px;
    }

    .Exit {
        position: relative;
        bottom: 650px;
        left: 1600px;
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
    }
    .displayCMT {
        position: relative;
        left: 1300px;
        bottom: 500px;
    }
    .name{
        position: relative;
        right: 480px;
        top: 70px;
    }
    .post{
        position: relative;
        top: 10px;
    }
    .sp{
        position: relative;
        left: 100px;
        font-size: 50px;
    }
</style>
<body>
    <div>
        <?php
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "webbanhang";
        $conn = mysqli_connect($servername, $username, $password, $dbname);
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        session_start();
        $id = $_GET['id'];
        // $id = mysqli_real_escape_string($conn, $id);
        $_SESSION['id'] = $id;
        $sql = "SELECT * FROM products WHERE id = '$id'";
        $result = mysqli_query($conn, $sql);
        if (mysqli_num_rows($result) > 0) {
            // Hiển thị thông tin sản phẩm
            while ($row = mysqli_fetch_assoc($result)) {
                $name=$row["name"];
                $price=$row["price"];
                $image=$row["image_url"];
                echo " <div>";
                echo'<h3 class="sp">'.$row["name"].'</h3>';
                echo "<img src='" . $row["image_url"] . "' height = 600px witdh = 600px />";
                echo'<h3 class="sp">Giá '.$row["price"].'</h3>';
                echo" <form method='POST' action='../cart/add.php'>";
                echo"<input style='width: 230px;height: 40px; position:relative; bottom: 50px;' type='submit'  value='Thêm vào giỏ hàng'>";
                echo"<input type='hidden' name='name_pro' value='$name' > ";
                echo "<input type='hidden' name='price_pro' value=$price >";
                echo"</form> ";
                echo" </div>";
            }
        } else {
            echo "Không có sản phẩm nào";
        }
        // echo "SELECT * FROM products WHERE id = '$id'";
        ?>
        <div>
            <form class="formPostCMT" action="../comment/post_commentsp.php" method="post">
                <tr>
                    <td>
                        <textarea name="comment" rows="5" cols="30" placeholder="Please enter your comment"
                            required></textarea>
                    </td>
                </tr>
                <tr>
                    <td><input class="post" style="width: 230px;height: 40px; position:relative; bottom: 50px;" type="submit" name="submit" value="Post"></td>
                </tr>
                <tr>
                <textarea class="name" name="name" rows="3" cols="30" placeholder="Please enter your name"
                            required></textarea>
                </tr>
            </form>
            <?php
              if(isset($_SESSION['username'])) {
                    echo'<a href="../ListSP/displayproduct.php" class="Exit">Close</a>';
                    echo'<a href="../ListSP/displayproduct.php" class="Exit1">  <img height="160px" src ="../../images/giohang.png"></a> ';
                }
                else{
                    echo'<a href="../index.php" class="Exit">Close</a>';
                }
            ?>
        </div>


        <div class="displayCMT">
            <?php
            $sql = "SELECT * FROM commentsp where product_id = '$id'";
            $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    $id = $row['id'];
                    $name = $row['user_name'];
                    $comment = $row['comment_text'];
                    echo "<li><strong>$name:</strong> $comment <form method='POST' action='../Comment/delete_commentsp.php'><input type='hidden' name='comment_id' value='$id'><button type='submits'>Xóa</button></form></li>";
                }
            } else {
                echo "Không có bình luận nào.";
            }
            $conn->close();
            ?>
        </div>
    </div>
</body>

</html>