# 0204_homework



## 1. Semantic Tag

```typescript
header, section, footer
```

## 2. input Tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
    <!-- 인라인 설정 넣기 -->
    <style>
    .pwd {
      display: inline
    }
    
    .login-button {
      display: inline
    }
  </style>
<body>
  <form action="">
    <div class="username">
      <label for="username">USERNAME : </label>
      <input placeholder="아이디를 입력해주세요." type="text" id="username">
    </div>
    <div class="pwd">
      <label for="pwd">PWD : </label>
      <input type="password" id="pwd" name="pwd">
    </div>
    <div class="login-button">
      <button type="submit">로그인</button>
    </div>

  </form>
</body>
</html>
```

`USERNAME`을 클릭하면 아이디를 입력하는 input에, `PWD` 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 시키는 방법은 `<label>`의 `for`에 상응하는 `<input>`의 `id` 값을 페어해주는 것이다.

`<input>`에 `placeholder=""`를 지정해주면 input 칸 안에 입력된 문구가 희미하게 나타난다.

## 3. 크기 단위

```typescript
em => 부모 요소에서 상속
rem => 부모 요소에서 상속 받지 않고 최상위 요소 (html) 만 기준으로 삼는다
```

## 4. 선택자

* 자손 결합자

  * `div` 셀렉터 하위의 모든 `p` 셀렉터의 요소가 영향을 받는다

    ```css
    div p {
    	color: crimson;
    }
    ```

* 자식 결합자

  * `div` 셀렉터 바로 아래의 `p` 셀렉터의 요소만 영향을 받는다

    ```css
    div > p {
        color: crimson;
    }
    ```