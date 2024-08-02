#include <stdio.h>
#include <stdlib.h>

int main(void){
        int hr1,min1,sec1;
        scanf("%d:%d:%d", &hr1, &min1, &sec1);

        int hr2,min2,sec2;
        scanf("%d:%d:%d", &hr2, &min2, &sec2);


        int hr3 = 0, min3, sec3;

        int total_secs1 = 0;
        total_secs1 += (hr1*3600);
        total_secs1 += (min1*60);
        total_secs1 += (sec1);

        int total_secs2 = 0;
        total_secs2 += (hr2*3600);
        total_secs2 += (min2*60);
        total_secs2 += (sec2);

        if (hr2 < hr1)
                total_secs2 += (24*3600);
        if (hr2 == hr1 && (min2 <= min1 && sec2 <= sec1))
                total_secs2 += (24*3600);
        int total_secs = (total_secs2-total_secs1);
        hr3 = (total_secs)/3600;
        total_secs -= hr3*3600;
        min3 = (total_secs)/60; total_secs -= min3*60;
        sec3 = total_secs;

        printf("%.2d:%.2d:%.2d", hr3, min3, sec3);
}
