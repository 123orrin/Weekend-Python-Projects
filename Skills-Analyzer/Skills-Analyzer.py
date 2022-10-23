"""
Skills Analysis
By Orrin Dahanaggamaarachchi

This program was created to analyze which skills are most important for me to learn to be successful in research and year 4 of Engineering Science.
Here are a few terms to note:
 - COLLECTION refers to an area of skills
 - ITEM refers to a specfic instance of a collection
 - SKILL refer to a skill in an item
For Example, thesises is a collection, a single thesis is an item, and a skill is a skill desired by that thesis
"""

engsci_thesis_collection = [['matlab', 'control theory', 'ECE356', 'ECE557'], ['signals', 'control theory', 'linear algebra'], ['linear algebra', 'math modeling', 'control systems', 'data science', 'medical applications'], ['linear algebra', 'math modeling', 'probability', 'control theory'], ['matlab', 'c/c++', 'linux', 'medical imaging', 'segmentation software'], ['matlab', 'c/c++', 'linux', 'medical imaging', 'segmentation software'], ['deep learning', 'medical imaging', 'computer vision', 'statistics', 'natural language processing'], ['video processing', 'python', 'pytorch', 'supervised learning', 'sequential learning', 'deep learning', 'machine learning', 'signal processing'], ['video processing', 'python', 'pytorch', 'supervised learnign', 'sequential learning', 'deep learning', 'machine learning'], ['matlab', 'control theory', 'depp learning', 'reinforcement learning', 'supervised learning', 'unsupervised learning', 'python'], ['c/c++', 'python', 'embedded systems', 'PCB design'], ['circuits', 'electromagnetism', 'embedded systems', 'PCD design', 'c/c++'], ['python', 'fluid mechnanics', 'git'], ['fluid mechanics', 'python', 'r', 'data science'], ['robotics', 'signal processing', 'data science']]

software_intern_collection = [['python', 'groovy', 'bash', 'linux', 'git'], ['c#', 'java', 'c/c++', 'python', 'html', 'css', 'javascript', 'sql', 'relational databases', '.net'], ['java', 'python', 'linux', 'cloud'], ['c/c++', 'python', 'ruby', 'matlab', 'ros', 'sql'], ['java', 'c/c++', 'c#'], ['html', 'css', 'javascript', 'bootstrap', 'react', 'c#', 'python', 'vb', 'sql', 'relational databases'], ['c/c++', 'linux'], ['c#', 'python', 'javascript', 'react', 'angular', 'cloud'], ['java', 'c/c++', 'python'], ['c#', 'git', 'angular', 'javascript', 'html', 'rest apis', 'azure', '.net'], ['java', 'c/c++', 'python', 'linux'], ['sql', 'django', 'flask', 'distributed systems', 'rest apis', 'git', 'python', 'linux'], ['c/c++', 'linux', 'git', 'embedded systems', 'python', 'ros']]

robotics_intern_collection = [['python', 'c/c++', 'ros', 'git', 'gazebo', 'lua', 'embdedded systems'], ['java', 'python', 'c/c++', 'git', 'linux', 'embedded systems', 'computer vision', 'machine learning'], ['control theory', 'cad', 'circuits'], ['computer vision', 'c/c++', 'linux', 'ros', 'tensorflow'], ['c#', 'python', 'java', 'sql', 'relational databases'], ['python', 'javascript', 'linux', 'circuits', 'soldering', 'ros', 'c/c++', 'embedded systems'], ['computer vision', 'deep learning', 'motion planning', 'control theory', 'embedded systems', 'distributed systems', 'c/c++', 'python'], ['c/c++', 'ros', 'git', 'jira', 'docker'], ['python', 'c/c++', 'ros', 'git', 'linux', 'gazebo', 'lua'], ['state estimation', 'computer vision', 'slam', 'machine learning', 'target detection', 'control theory', 'c/c++', 'linux', 'ros', 'tensorflow', 'gazebo', 'pcl'], ['linux', 'python', 'django', 'flask', 'rest apis', 'git', 'ros', 'distributed systems'], ['cad', 'solidworks', 'ros', 'c/c++', 'python', 'linux'], ['c/c++', 'ros', 'git', 'aws', 'docker', 'jira']]

aerospace_intern_collection = [['siemens nx', 'solidworks', 'cad', 'python', 'c/c++'], ['c#', '.net', 'go', 'git', 'jira', 'scrum'], ['c#', '.net', 'javascript', 'react', 'angular', 'git', 'jira', 'scrum'], ['siemens nx', 'cad', 'solidworks', 'python', 'c/c++'], ['python', 'linux', 'git', 'jira', 'scrum', 'embedded systems', 'c/c++'], ['javascript', 'angular', 'react', 'node.js', 'git', 'jira', 'linux', 'scrum'], ['soldering', 'wire harnessing', 'multimeters', 'oscilloscopes', 'cad','solidworks', 'python', 'c/c++', 'ros', 'altium']]

engineering_intern_collection = [['circuits', 'python'], ['cad'], ['cad'], ['c/c++', 'java', 'golang', 'rest apis', 'angular', 'react', 'matlab', 'docker', 'kubernetes', 'rancher']]

GNC_collection = [['computer vision', 'ros', 'control theory', 'math modelling'], ['control theory', 'matlab', 'simulink', 'c/c++'], ['c/c++', 'ros', 'git', 'jira'], ['c/c++', 'matlab', 'simulink', 'linux', 'python'], ['matlab', 'simulink', 'c/c++', 'python'], ['matlab', 'simulink'], ['matlab', 'stk'], ['ros', 'c/c++', 'python', 'linux', 'deep learning', 'pytorch', 'tensorflow'], ['matlab', 'simulink', 'c/c++', 'embedded systems']]

def get_popular_skills(*skill_collections):
    popular_skills = {}

    for collection in skill_collections:
        for item in collection:
            for skill in item:
                if skill in popular_skills:
                    popular_skills[skill] = popular_skills[skill] + 1
                else:
                    popular_skills[skill] = 1
    
    return popular_skills


def get_key_from_value(popular_skills, value_to_find):
    for key, value in popular_skills.items():
         if value_to_find == value:
             return key


def print_popular_skills(popular_skills, equal_to_or_greater_than=1):
    for value in sorted(popular_skills.values(), reverse=True):
        key = get_key_from_value(popular_skills, value)
        if value >= equal_to_or_greater_than:
            print(f'{key}: {popular_skills[key]}')
        del popular_skills[key]

if __name__ == '__main__':
    popular_skills = get_popular_skills(engsci_thesis_collection, software_intern_collection, robotics_intern_collection, aerospace_intern_collection, engineering_intern_collection, GNC_collection)
    print_popular_skills(popular_skills, 3)
