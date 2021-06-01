#Group Project – Part 2
data <- read.csv(file = "data.csv")
mydata <- data[,c(2:5,7:9,11:12)] #Select variables
head(mydata)
summary(mydata) #View summary
sum(is.na(mydata)) #Count missing values for all variables. There are no missing values in this particular dataset.

#Draw basic scatterplot for variables radius_mean and texture_mean
plot(mydata$radius_mean, mydata$texture_mean,
     xlab = "radius_mean", ylab = "texture_mean")
rug(mydata$radius_mean, side = 1) #Draw rug symbols on horizontal axis
rug(mydata$texture_mean, side = 2) #Draw rug symbols on vertical axis
text(mydata$radius_mean, mydata$texture_mean, cex = 0.8, labels = abbreviate(row.names(mydata)), pos = 3) #Add labels to plot
#From observing the plot, points 240, 462, 181, 213, and 353 appear to be outliers.

#Draw univariate (conventional) boxplot for variables radius_mean and texture_mean
boxplot(mydata$radius_mean)
boxplot(mydata$texture_mean)
#From observing the univariate boxplots, there appears to be approximate 13 outliers in radius_mean and approximately 7 outliers in texture_mean



#Draw bivariate boxplot 
mydata <- mydata[, c("radius_mean", "texture_mean")] #Extract variables radius_mean and texture_mean
#mydata <- mydata[,2:3] #Another way to extract the variables
#Load MVA package
bvbox(mydata, xlab = "radius_mean", ylab = "texture_mean")
text(mydata$radius_mean, mydata$texture_mean, cex = 0.8, labels = abbreviate(row.names(mydata)), pos = 3) #Add labels to plot
#There are more points that are outliers: 240, 233, 260, 220, 266, 83, 462, 522, 123, 181, 353, and 213.

#Compute correlation with outliers
cor(mydata$radius_mean, mydata$texture_mean)

#Draw bivariate bloxplot and label outliers in red
lab <- match(c("240", "233", "260", "220", "266", "83", "462", "522", "123", "181", "353", "213"), row.names(mydata)) #Create object for outliers
outlier <- match(lab, rownames(mydata)) #Match object outliers to original dataset
text(mydata$radius_mean[outlier], mydata$texture_mean[outlier], cex = 0.8, labels = abbreviate(lab), col = "red", pos = 3) #Label outliers in red.

#Remove outliers from variables
radius_mean <- mydata$radius_mean[-outlier]
texture_mean <- mydata$texture_mean[-outlier]

#Correlation without outliers
cor(radius_mean, texture_mean)
# The correlation coefficient between the two variables slightly decreased from, 0.3237819 to 0.3222082 after excluding the variables indicating a slightly weaker correlation between the two variables as the correlation coefficient approaches 0.
