a=a+1
plot 'bubble_fancy.txt' index a using 1:2 with impulses lw 3 notitle;
pause 0.2
if(a < b - 1) reread
