import { defineStore } from "pinia";
import { DefaultService } from "../providers";
import { router } from "../main";

function getRandomInt(max: number) {
  return Math.floor(Math.random() * max);
}

const useQuizStore = defineStore("Quiz", {
  state: () => {
    return {
      isGameJoined: false,
      isSignedIn: false,
      userId: 53,
      io: undefined,
      isRoomAdmin: false,
      adminToken: undefined,
      hasResponded: false,
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
      lobbies: new Array<any>(),
      players: new Array<any>(),
      question: <any>{},
      correctResponse: <any>{},
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
    new_player_joined(user: any) {
      if (!this.players.includes(user.name)) {
        this.players.push(user.name);
      }
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
      this.isGameJoined = true;
      this.lobbyToken = lobbyToken;
      (this.io as any).emit("enter_quiz", {
        player_token: lobbyToken,
        name: this.name,
      });
    },
    launchGame() {
      (this.io as any).emit("start_quiz", {
        player_token: this.lobbyToken,
        admin_token: this.adminToken,
      });
    },
    addRoom(lobbyToken: string) {
      (this.io as any).emit("new_room_added", {
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
        console.log(data[i]);
        this.lobbies.push({
          lobbyToken: data[i].player_token,
          numberPlayers: data[i].number_players,
          quizName: data[i].quiz_name,
        });
      }
    },
    player_list(data: any) {
      for (let i = 0; i < data.data.length; i++) {
        if (!this.players.includes(data.data[i])) {
          this.players.push(data.data[i]);
        }
      }
    },
    send_question(data: any) {
      this.question = data.data;
      this.hasResponded = false;
      this.correctResponse = [];
      router.push(`/quiz/${this.lobbyToken}`);
      // {
      //   "data": {
      //     "question": {
      //       "content": "zerzerze",
      //       "question_id": 3,
      //       "number_question": 3
      //     },
      //     "responses": [
      //       {
      //         "id": 4,
      //         "content": "rezrzerg"
      //       },
      //       {
      //         "id": 3,
      //         "content": "rezrze"
      //       },
      //       {
      //         "id": 7,
      //         "content": "rezrze"
      //       },
      //       {
      //         "id": 11,
      //         "content": "rezrzerze"
      //       }
      //     ]
      //   }
      // }
    },
    respondQuestion(selected: number) {
      (this.io as any).emit("receive_response", selected);
    },
    stop_sending() {
      this.hasResponded = true;
    },
    correct_response(data: any) {
      this.correctResponse = Object.values(data);
    },
  },
});

export default useQuizStore;
