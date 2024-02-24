import streamlit as st
import tbapy

#with match number and team position get robot number
def generate_csv(scouter_initials, match_number, robot, team_number, human_player_toggle, no_show,
        auto_mobility, auto_amp_scored, auto_amp_missed, auto_speaker_scored, auto_speaker_missed, auto_foul,
        cooperation, teleop_amp_scored, teleop_amp_missed, teleop_speaker_scored, teleop_speaker_missed, note_in_trap, teleop_foul,
        end_position, harmony, offensive_skill, defensive_skill, died, tipped_over, card, comments):
    csv_content = f"{scouter_initials}\t{match_number}\t{robot}\t{team_number}\t{human_player_toggle}\t{no_show}\t{auto_mobility}\t{auto_amp_scored}\t{auto_amp_missed}\t{auto_speaker_scored}\t{auto_speaker_missed}\t{auto_foul}\t{cooperation}\t{teleop_amp_scored}\t{teleop_amp_missed}\t{teleop_speaker_scored}\t{teleop_speaker_missed}\t{note_in_trap}\t{teleop_foul}\t{end_position}\t{harmony}\t{offensive_skill}\t{defensive_skill}\t{died}\t{tipped_over}\t{card}\t{comments}"
    
    return csv_content

def get_robo(event,match_level,match_number,robot_pos):
    api_key = '3hJGWwBnRwxPVXtFiThp8n1dEuuMgcOg0xMLm41dPNsgIbL7mKpeAZF11bTaUWR7'
    tba = tbapy.TBA(api_key)
    if match_level == "Quals":
        match_indicator = "_qm"+str(match_number)
    match = tba.match(key=event+match_indicator)
    if str(robot_pos).startswith("Red"):
        team_color = "red"
    else:
        team_color = "blue"
    team_list = match['alliances'][team_color]["team_keys"]
    index = int(robot_pos[-1]) - 1 
    return team_list[index] 

def main():
    st.set_page_config(layout="wide")
    st.title("This is stupid")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader("Prematch")
        event_name = st.text_input("Event")
        match_level_pos = ["Quals","Semifinals","Finals"]
        match_level = st.selectbox("Match level",match_level_pos)
        scouter_initials = st.text_input("Scouter Initials")
        match_number = st.number_input("Match Number",value=None,step=1)
        robot_pos = ["Red 1","Red 2","Red 3","Blue 1","Blue 2","Blue 3"]
        robot = st.selectbox("Robot",robot_pos)
        val = 0
        if robot and event_name and match_level and match_number:
            val = get_robo(event_name,match_level,match_number,robot_pos)
        team_number = st.number_input("Team Number",value=val)
        human_player_toggle = st.toggle("Human Player at AMP")
        no_show = st.toggle("No Show")

    with col2:
        st.subheader("Autonomous")
        auto_mobility = st.toggle("Mobility?")
        auto_amp_scored = st.number_input("Amp Scored", key="1",value=0)
        auto_amp_missed = st.number_input("Amp Missed",key="2",value=0)
        auto_speaker_scored = st.number_input("Speaker Scored",key="3",value=0)
        auto_speaker_missed = st.number_input("Speaker missed",key="4",value=0)
        auto_foul = st.number_input("Auto foul",value=0)

    with col3:
        st.subheader("Teleop")
        cooperation = st.toggle("Cooperation")
        teleop_amp_scored = st.number_input("Amp Scored",key="5",value=0)
        teleop_amp_missed = st.number_input("Amp Missed",key="6",value=0)
        teleop_speaker_scored = st.number_input("Speaker Scored",key="7",value=0)
        teleop_speaker_missed = st.number_input("Speaker missed",key="8",value=0)
        note_in_trap = st.number_input("Note in trap?",value=0)
        teleop_foul = st.number_input("Teleop foul",value=0)

    with col4:
        st.subheader("Endgame")
        end_position = st.selectbox("End Position",["No Climb","Failed Climb","Parked","Onstage","Spotlight"])
        harmony = st.selectbox("Harmony",["First on chain","Second on chain","Third on chain"])

    with col5:
        st.subheader("Postmatch")
        offensive_skill = st.selectbox("Offensive Skill",["Not effective","Average","Very Effective","Not Observed"])
        defensive_skill = st.selectbox("Defensive Skill",["Not effective","Average","Very Effective","Not Observed"])
        died = st.toggle("Died")
        tipped_over = st.toggle("Tipped over")
        card = st.selectbox("Yellow/Red card",["No Card","Yellow Card","Red Card"])
        comments = st.text_input("Comments")
    
    if st.button('Commit'):
        # Process inputs and generate CSV content
        csv_content = generate_csv(scouter_initials, match_number, robot, team_number, human_player_toggle, no_show,
        auto_mobility, auto_amp_scored, auto_amp_missed, auto_speaker_scored, auto_speaker_missed, auto_foul,
        cooperation, teleop_amp_scored, teleop_amp_missed, teleop_speaker_scored, teleop_speaker_missed, note_in_trap, teleop_foul,
        end_position, harmony, offensive_skill, defensive_skill, died, tipped_over, card, comments)
        
        # Display the CSV content
        st.text_area('CSV Output', value=csv_content, height=200)
        st.code(Path, language="python")


if __name__ == "__main__":
    main()

