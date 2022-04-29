class Type(object):
    ISSUE=1
    FEATURE=2
    CHOICES = (
        (ISSUE,'Issue'),
        (FEATURE,'Feature'),
    )

class Priority(object):
    CAB_HIGH=1
    MEDIUM=2
    LOW=3
    CHOICES = (
        (CAB_HIGH,'Cab High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
class Status(object):
    TODO=1
    INPROGRESS=2
    INREVIEW=3
    CLOSED=4
    CHOICES = (
        (TODO,'Todo'),
        (INPROGRESS,'In Progress'),
        (INREVIEW,'In Review'),
        (CLOSED,'Closed')
    )
