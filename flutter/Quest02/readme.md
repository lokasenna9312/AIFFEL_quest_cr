# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 윤경석, 공옥례
- 리뷰어 : 김해원, 류지호


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        ![1번](https://github.com/user-attachments/assets/9aa96068-429d-4618-8019-84aa15abd58b)
    
- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        
- [ ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        
- [ ]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
      ![5번](https://github.com/user-attachments/assets/64fbea02-3102-42f0-98cd-b8ba58b0c3ff)

      Container를 알아보기 깔끔하게 작성해주셨습니다.


# 회고(참고 링크 및 코드 개선)
```
다트 처음 실행하면 나오는 디폴트 코드를 그대로 가져가시는 부분이 아쉽습니다.
실제 프론트를 구현하는데에 있어 불필요한 요소들이 많아 효율성을 떨어뜨리는 것 같습니다.
다음에는 더욱 깔끔한 구현을 기대하겠습니다. :)

주어진 시간 안에 원하는 결과를 성공적으로 도출해내셨습니다.
1개의 class가 아닌, 2개의 class를 사용하신 점이 인상깊었고,
이에 대해 대화를 나누고 추가로 조사를 하며 복잡한 app을 구현할수록 더 많은 class를 사용하는 것이 유지 보수에 유리하다는 점도 학습할 수 있었습니다.
직접 상세하게 작성하신 주석, 에러가 난 부분에 대해 남겨진 기록, 회고가 없다는 점이 아쉬웠지만 직접 구두로 잘 설명해주셨습니다.

안드로이드 스튜디오가 아닌 다른 임시 환경에서도 원하는 결과물을 도출해내신 것으로 보아,
충분히 이후 개인 학습을 통해 새로운 시도와 추가 실험을 해보실 수 있을 것 같습니다.

class를 2개 사용하신 것 외에는 중복되는 코드나 불필요한 부분 없이 잘 작성해주셨습니다.

```
