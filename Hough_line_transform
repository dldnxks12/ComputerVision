img = cv2.imread('gayoung.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# lines : 17462개 x (거리, 각도)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.cos(theta)
    x0 = a*rho  # x0 = rho*cos(theta) # 시작점 x 좌표
    y0 = b*rho  # y0 = rho*sin(theta) # 시작점 y 좌표
    
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))    
    
    cv2.line(img,(x1,y1), (x2,y2), (0,0,255), 1)
    
cv2.imshow('edges', edges)
cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()
