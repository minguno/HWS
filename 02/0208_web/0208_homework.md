# 0208_homework

## 1. CSS flex-direction

1. `row`: 왼쪽에서 오른쪽 나열
2. `reverse-row`: 오른쪽에서 왼쪽 나열
3. `column`: 위에서 아래로 나열
4. `reverse-column`: 아래에서 위로 나열

## 2. BootStrap flex-direction

1. `flex-row`
2. `flex-reverse-row`
3. `flex-column`
4. `flex-reverse-column`

## 3. align-items

1. `stretch`: 기본값; 컨테이너 가득
2. `flex-start`: 맨 위
3. `flex-end`: 맨 아래
4. `center`: 가운데
5. `baseline`: 텍스트 baseline 기준

## 4. flex-flow

`flex-direction`과 `flex-wrap`의 축약형이다

## 5. BootStrap Grid System

```html
<div class="container">
    <div class="row">
        ..
    </div>
</div>
```

## 6. Breakpoint prefix

BootStrap의 `row`는 기본적으로 12  `column`을 갖는다.

반응형 웹 설계를 위해 특정 해상도 이상일 때 적용되는 설정을 각각 넣어주는데 제일 작은 범위인 `xs`는 prefix를 생략한다. 그 외엔 `sm`, `md`, `lg`, `xl`, `xxl` 의 prefix를 넣는다. 각 해상도 범위가 바뀔 때 마다 12칸의 너비 범위 또한 반응하기 위한 구분이다. 특정 해상도 이상의 값에 항상 적용되며 `.offset-`, `.row-col-` 에도 동일하게 적용된다.

한 `row` 대해 몇 칸을 차지할 건지에 대한 입력값이다. 꼭 한 `column`이 12를 채워야 하는 것은 아니며, 빈 부분은 공백 처리된다. `container`를 가득 채운 2 개의 `column` 을 원하면 각각 `.col-6`을 입력하면 된다. 정수 단위로만 사용된다. 생략하고 그냥 `.col` 처리만 하면 자동으로 width가 equally distributed 된다.



