required_skills = ["Python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
	if any(skill_name.casefold() == skill.casefold() for skill in required_skills):
		return "Skill available"
	return "Skill not available"


skill_name = input("Enter a skill name: ").strip()
print(check_skill(skill_name))