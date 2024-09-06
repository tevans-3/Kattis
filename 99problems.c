#include <stdio.h>
#include <stdlib.h>

int main(void){
        int N;
        scanf("%d", &N);
        int M = N;
        int R = N;

        while ((M%100)!= 99 && M >0){
                M--;
        }
        while ((R%100)!=99){
                R ++;
        }

        int max = 0;
        if (abs(N-abs(M)) < R-N && (M%100)==99){
                max = M;
        }
        else if ((R%100) == 99){
                max = R;
        }
        printf("%d", max);
}
