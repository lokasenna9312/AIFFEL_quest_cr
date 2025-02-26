import 'dart:async';

import 'package:flutter/material.dart';

int study_minutes = -1;
int break_minutes = -1;
int study_time = 3;
int break_time = 3;
int break_time_4th = 5;
int circuit = 0;
int long_break = 4;

void main() {
  Timer.periodic(Duration(minutes: 1), counter);
}

bool? is_now_break(){
  if(circuit == 0){
    print("포모도로 타이머 작동을 시작합니다.");
    study_minutes = 0;
    circuit += 1;
    print("$circuit 교시 시작합니다.");
    return false;
  }
  else if(break_minutes == -1 && study_minutes < study_time){
    return false;
  }
  else if(circuit != long_break && study_minutes == study_time){
    print("공부 시간이 끝났습니다.");
    what_time_is_it_now();
    study_minutes = -1;
    break_minutes = 0;
    return true;
  }
  else if(circuit != long_break && study_minutes == -1 && break_minutes < break_time){
    return true;
  }
  else if(circuit != long_break && break_minutes == break_time) {
    print("쉬는 시간이 끝났습니다.");
    what_time_is_it_now();
    break_minutes = -1;
    study_minutes = 0;
    circuit += 1;
    print("$circuit 교시 시작합니다.");
    return false;
  }
  else if(circuit == long_break && study_minutes == study_time){
    print("4번째 쉬는 시간이므로 15분 휴식합니다.");
    what_time_is_it_now();
    study_minutes = -1;
    break_minutes = 0;
    return true;
  }
  else if(circuit == long_break && study_minutes == -1 && break_minutes < break_time_4th){
    return true;
  }
  else if(circuit == long_break && break_minutes == break_time_4th){
    print("쉬는 시간이 끝났습니다.");
    what_time_is_it_now();
    break_minutes = -1;
    study_minutes = 0;
    circuit += 1;
    print("$circuit 교시 시작합니다.");
    return false;
  }
}

void counter(Timer){
  if(is_now_break() == false) {
    study_counter();
  }else if(is_now_break() == true){
    break_counter();
  }
}

void what_time_is_it_now(){
  DateTime now = DateTime.now();
  print("현재 시각은 $now 입니다.");
}

void study_counter(){
  study_minutes += 1;
  print("공부 시간이 $study_minutes 분 흘렀습니다.");
}

void break_counter(){
  break_minutes += 1;
  print("쉬는 시간이 $break_minutes 분 흘렀습니다.");
}
