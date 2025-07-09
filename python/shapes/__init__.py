# shapes/__init__.py
# from shapes import circle, rectangle
# from shapes import * (고객이 불러쓰는 게 싫을 경우에는 all에서 하나를 빼버려도 됨.)

__all__ = ["circle", "rectangle"]

#shapes라는 패키지를 부르기 전에 init 파일 먼저 읽는다. __all__이라는 스페셜메소드에 있는 것만 고객이 쓸 수 있음. 