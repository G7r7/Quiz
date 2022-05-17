import { defineStore } from "pinia";
import { inject } from "vue";

const useQuizStore = defineStore("Quiz", {
  state: () => {
    return {
      actualQuestion: 1,
      timer: 0,
      quizName: "tatata",
      quizId: 3320,
      players: [{ userId: 0, isDone: true }],
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
      this.players = this.players.map((player) => ({
        ...player,
        isDone: false,
      }));
    },
    userJoined(user: any) {
      this.players.push(user);
    },
    userLeft(user: any) {
      this.players = this.players.filter(
        (player) => player.userId !== user.userId
      );
    },
    // newMessage(message: any) {
    //   this.messages.push(message);
    // },
    userDone(user: any) {
      const i = this.players.findIndex(
        (player) => player.userId === user.userId
      );
      this.players[i].isDone = true;
    },
    timeOut() {
      const { io }: any = inject("vuePiniaWS");
      const responseIds = this.question.responses
        .filter((response) => response.isSelected)
        .map((response) => response.id);
      if (this.question.multiple_answers) {
        io.emit("response", responseIds);
      } else {
        io.emit("response", responseIds[0]);
      }
    },
    timer(data: any) {
      this.timer = data.timer;
    },
    score(data: any) {
      this.score = data;
    },
  },
});

export default useQuizStore;
