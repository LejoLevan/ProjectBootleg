class QuestChecker:
    """Complies all quests trackers and keeps track on status on quests"""
    def __init__(self, data):
        self.ongoing_quests = data['ongoingQuests']
        self.completed_quests = data['completedQuests']
    
    def appendongoing(self, questname):
        """Method to make a quest ongoing"""
        self.ongoing_quests.append(questname)
    
    def appendcompleted(self, questname):
        """Method ot make a quest completed"""
        if questname in self.ongoing_quests:
            self.ongoing_quests.remove(questname)
        self.completed_quests.append(questname)
    def combatquestsUpdate(self):
        #methods to check combat quests go here (ex. self.randomquest.check())
    
    def questsUpdate(self):
        #methods to check regular quest go here
 