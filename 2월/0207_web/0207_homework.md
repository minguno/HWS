# 0207_homework



[Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)의 Components 예시를 보고 빈 칸 채우기

## 1. Components: Button

![image-20220207211957103](0207_homework.assets/image-20220207211957103.png)

```html
<button type="submit" class="btn btn-success">Sign in</button>
```

a) `btn`: `button` 요소와 함께 쓰이도록 설정된 클래스 (`a`나 `input` 요소와도 함께 사용 가능하다)

## 2. Components: Navbar

![image-20220207212016071](0207_homework.assets/image-20220207212016071.png)

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  ..
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        ..
        </ul>
     </div>
  ..
</nav>
```

a) `dark`: 밝은 글씨색과 어두운 바탕색 설정

b) `navbarNavDropdown`: 상위 `button` 태그에 `data-bs-target` 값이 `#navbarNavDropdown`이기 때문에 같은 값으로 연결

c) `navbar-nav`: 라인의 full-height와 lightweight navigation을 도와줌

## 3. Components: Pagination

![image-20220207211901767](0207_homework.assets/image-20220207211901767.png)

```html
<nav>
  ..
    <ul class="pagination">
        <li class="page-item disabled">
          ..
        </li>
        <li class="page-item active" aria-current="page">
          ..
        </li>
        ..
    </ul>
  ..  
</nav>
```

a) `pagination`: 여러개의 연속된 페이지 번호를 나타내고 있기 때문

b) `disabled`: `Prev` 같은 경우 글씨가 바래지고 클릭이 불가능하기 때문

c) `active`: 현재 위치한 페이지가 파란색으로 표시되기 때문에 `1`을 나타내는 `a` 태그의 부모 요소에 표시해준다
