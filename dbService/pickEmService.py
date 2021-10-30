from dbService.models.userModel import UserModel
from dbService.models.teamModel import TeamModel
from dbService.models.picems import TeamsPickEmModel

from typing import List, Optional, Dict


def add_new_user(t_id: int, name: str):
    user = UserModel.create(t_id=t_id, name=name)

    return user.get_id()


def get_user(t_id: int) -> Optional[UserModel]:
    return UserModel.get_or_none(t_id=t_id)


def add_team(team_name: str):
    team = TeamModel.create(name=team_name)

    return team.get_id()


def get_all_teams() -> List[str]:
    query = TeamModel.select()
    teams = [team.name for team in query]

    return teams


def save_pick_em(user_t_id: int, best: str, worst: str, top7: List[str]):
    user = get_user(user_t_id)
    if user is not None:
        best_team = TeamModel.get(name=best)
        worst_team = TeamModel.get(name=worst)
        team2 = TeamModel.get(name=top7[0])
        team3 = TeamModel.get(name=top7[1])
        team4 = TeamModel.get(name=top7[2])
        team5 = TeamModel.get(name=top7[3])
        team6 = TeamModel.get(name=top7[4])
        team7 = TeamModel.get(name=top7[5])
        team8 = TeamModel.get(name=top7[6])

        TeamsPickEmModel.create(best_team=best_team, worst_team=worst_team,
                                team2=team2, team3=team3,
                                team4=team4, team5=team5,
                                team6=team6, team7=team7,
                                team8=team8, user=user)


def get_users_pick_em(user_t_id: int) -> Optional[Dict]:
    user = get_user(user_t_id)
    if user is not None:
        pick_em = TeamsPickEmModel.get_or_none(user=user)
        if pick_em is None:
            return None
        else:
            return {"best": pick_em.best_team.name,
                    "worst": pick_em.worst_team.name,
                    "top7": [pick_em.team2.name, pick_em.team3.name,
                             pick_em.team4.name, pick_em.team5.name,
                             pick_em.team6.name, pick_em.team7.name,
                             pick_em.team8.name]}
