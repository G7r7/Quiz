import { defineStore } from "pinia";
import { DefaultService } from "../providers";

function getRandomInt(max: number) {
  return Math.floor(Math.random() * max);
}

const useQuizStore = defineStore("Quiz", {
  state: () => {
    return {
      isSignedIn: false,
      userId: 53,
      io: undefined,
      isRoomAdmin: false,
      adminToken: undefined,
      userQuizes: [
        {
          quiz_name: "TestQuiz",
          date_creation: "2022-05-19",
          id: 7,
        },
        {
          quiz_name: "testquizzzz",
          date_creation: "2022-05-19",
          id: 57,
        },
      ],
      name: `GUEST-${getRandomInt(50)}`,
      actualQuestion: 1,
      timer: 0,
      quizName: "tatata",
      quizId: 3320,
      lobbyToken: "",
      lobbies: [],
      players: [{ userId: 0, isDone: true, name: "borehurc" }],
      question: {
        quiz_id: 0,
        id: 0,
        content: "Ceci est une question ?",
        multiple_answers: true,
        totalTime: 30,
        responses: [
          {
            question_id: 0,
            id: 0,
            content: "oui",
            isSelected: false,
          },
        ],
      },
    };
  },
  actions: {
    newQuestion(question: any) {
      this.question = question;
      this.players = this.players.map((player: any) => ({
        ...player,
        isDone: false,
      }));
    },
    userJoined(user: any) {
      this.players.push(user);
    },
    userLeft(user: any) {
      this.players = this.players.filter(
        (player: any) => player.userId !== user.userId
      );
    },
    // newMessage(message: any) {
    //   this.messages.push(message);
    // },
    userDone(user: any) {
      const i = this.players.findIndex(
        (player: any) => player.userId === user.userId
      );
      this.players[i].isDone = true;
    },
    timeOut() {
      const responseIds = this.question.responses
        .filter((response: any) => response.isSelected)
        .map((response: any) => response.id);
      if (this.question.multiple_answers) {
        this.io && (this.io as any).emit("response", responseIds);
      } else {
        this.io && (this.io as any).emit("response", responseIds[0]);
      }
    },
    timer(data: any) {
      this.timer = data.timer;
    },
    score(data: any) {
      this.score = data;
    },
    joinLobby(lobbyToken: string) {
      this.lobbyToken = lobbyToken;
      this.io &&
        (this.io as any).emit("enter_quiz", {
          token: lobbyToken,
          name: this.name,
        });
    },
    start_quiz() {},
    send_question(question: any) {},
    launchGame() {
      this.io.emit("enter_quiz", {
        player_token: this.lobbyToken,
        name: this.name,
      });
      this.io.emit("start_quiz", {
        player_token: this.lobbyToken,
        admin_token: this.adminToken,
      });
    },
    addRoom(lobbyToken: string) {
      this.io.emit("new_room_added", {
        player_token: lobbyToken,
        quiz_name: this.quizName,
        number_players: 1,
      });
    },
    new_room_added(data: any) {
      this.lobbies.push({
        lobbyToken: data.player_token,
        quizName: data.quiz_name,
        numberPlayers: data.number_players,
      });
    },
    all_rooms(data: any) {
      const length = Object.keys(data).length;
      for (let i = 0; i < length; i++) {
        this.lobbies.push({
          player_token: data[i].player_token,
          numberPlayers: data[i].number_players,
          quizName: data[i].quiz_name,
        });
      }
    },
  },
});

export default useQuizStore;
