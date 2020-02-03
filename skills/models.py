from django.db import models
class Skill(models.Model):
	STATUS_CHOICES = (
	    ('fas fa-code','Code'),
	    ('fab fa-python','Python'),
	    ('fab fa-react','React'),
	    ('fab fa-css3-alt','Css3'),
	    ('fab fa-cuttlefish','C'),
	    ('fab fa-java','Java'),
	    ('fab fa-js-square','js'),
	    ('fab fa-linux','Linux'),
	    ('fab fa-php','Php'),
	    ('fas fa-ruler-combined','Ruler'),
	    ('fas fa-database','Database'),
	    ('fas fa-terminal','Shell'),
	    ('fab fa-node','Nodejs'),
	    ('fab fa-aws','AWS'),
	    ('fab fa-android','Android'),
	    ('fab fa-microsoft','Microsoft'),
	    ('fab fa-git','Git'),
	)
	PERCENTEAGE = (
		('40','40%'),
		('50','50%'),
		('60','60%'),
		('70','70%'),
		('80','80%'),
		('90','90%'),
		('95','95%'),
		('100','100%'),
		)
	title = models.CharField(max_length=100)
	description = models.TextField()
	progress = models.CharField(max_length=30,choices=PERCENTEAGE,default='100')
	code = models.CharField(max_length=30,choices=STATUS_CHOICES,default='Code')
	def __str__(self):
		return self.title
