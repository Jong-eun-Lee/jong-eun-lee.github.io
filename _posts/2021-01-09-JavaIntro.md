---
layout: post
title: Introduction
date: 2021-01-09 12:13:03 +0900
category: Java
---

# What is Java?
<br/><br/>
Java는 컴퓨터 프로그래밍 언어
JDK(개발도구) + JRE(실행환경) + API(라이브러리)
계속 버전이 업데이트 되고 있다.

---
# 자바의 특징
<br/><br/>
객체지향 언어
자동 메모리 관리(by Garbage Collector)(Garbage(Dangling Object)를 알아서 정리해 줘서 메모리가 부족하지 않게)
멀티 쓰레드를 지원(하나의 프로그램에서 여러 작업을)
풍부한 라이브러리
운영체제(OS)에 독립적(특정 운영체제에서 작성한 프로그램을 수정하지 않고도 다른 운영체제에서도 실행 가능)

---
# 자바 가상 머신(JVM)
<br/><br/>
여러 운영체제에서 자바로 만든 프로그램을 실행할 수 있는 이유?
-> JVM 덕분(Write once, run anywhere)
Java 애플리케이션 <-> JVM(Windows 용) <-> OS(like Windows) <-> 컴퓨터(하드웨어)
JVM이 없었다면 다른 운영체제에서 애플리케이션을 쓰려면 수정이 필요했을 것임.

---