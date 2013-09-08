import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'medic_1a':
		return

	actor.addSkill('expertise_me_vital_damage_3')

	actor.addSkillMod('expertise_damage_line_me_dm', 5)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'medic_1a':
		return

	actor.removeSkill('expertise_me_vital_damage_3')

	actor.removeSkillMod('expertise_damage_line_me_dm', 5)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
