/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Question } from "../models/Question";
import type { QuestionCreate } from "../models/QuestionCreate";
import type { Quiz } from "../models/Quiz";
import type { QuizCreate } from "../models/QuizCreate";
import type { Response } from "../models/Response";
import type { ResponseCreate } from "../models/ResponseCreate";
import type { User } from "../models/User";
import type { UserCreate } from "../models/UserCreate";
import type { UserLogged } from "../models/UserLogged";
import type { UserLogin } from "../models/UserLogin";

import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";

export class DefaultService {
  /**
   * Create User
   * @param requestBody
   * @returns User Successful Response
   * @throws ApiError
   */
  public static createUserUsersPost(
    requestBody: UserCreate
  ): CancelablePromise<User> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/users/",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Log User
   * @param requestBody
   * @returns UserLogged Successful Response
   * @throws ApiError
   */
  public static logUserUsersLoginPost(
    requestBody: UserLogin
  ): CancelablePromise<UserLogged> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/users/login",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Read Users
   * @param skip
   * @param limit
   * @returns User Successful Response
   * @throws ApiError
   */
  public static readUsersUsersListGet(
    skip?: number,
    limit: number = 100
  ): CancelablePromise<Array<User>> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/users/list",
      query: {
        skip: skip,
        limit: limit,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Read User
   * @param userId
   * @returns User Successful Response
   * @throws ApiError
   */
  public static readUserUsersUserIdGet(
    userId: number
  ): CancelablePromise<User> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/users/{user_id}",
      path: {
        user_id: userId,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Quiz
   * @param quizId
   * @returns Quiz Successful Response
   * @throws ApiError
   */
  public static getQuizQuizQuizIdGet(quizId: number): CancelablePromise<Quiz> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/quiz/{quiz_id}",
      path: {
        quiz_id: quizId,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Quizs
   * @param userId
   * @param skip
   * @param limit
   * @returns Quiz Successful Response
   * @throws ApiError
   */
  public static getQuizsQuizListUserIdGet(
    userId: number,
    skip?: number,
    limit: number = 100
  ): CancelablePromise<Array<Quiz>> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/quiz/list/{user_id}",
      path: {
        user_id: userId,
      },
      query: {
        skip: skip,
        limit: limit,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Create Quiz
   * @param requestBody
   * @returns Quiz Successful Response
   * @throws ApiError
   */
  public static createQuizQuizPost(
    requestBody: QuizCreate
  ): CancelablePromise<Quiz> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/quiz/",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Questions
   * @param quizId
   * @param skip
   * @param limit
   * @returns Question Successful Response
   * @throws ApiError
   */
  public static getQuestionsQuestionListQuizIdGet(
    quizId: number,
    skip?: number,
    limit: number = 100
  ): CancelablePromise<Array<Question>> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/question/list/{quiz_id}",
      path: {
        quiz_id: quizId,
      },
      query: {
        skip: skip,
        limit: limit,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Create Question
   * @param requestBody
   * @returns Question Successful Response
   * @throws ApiError
   */
  public static createQuestionQuestionPost(
    requestBody: QuestionCreate
  ): CancelablePromise<Question> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/question/",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Create Response
   * @param requestBody
   * @returns Response Successful Response
   * @throws ApiError
   */
  public static createResponseResponsePost(
    requestBody: ResponseCreate
  ): CancelablePromise<Response> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/response/",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }

  /**
   * Generate Token
   * @param userId
   * @param quizId
   * @param n
   * @param m
   * @returns any Successful Response
   * @throws ApiError
   */
  public static generateTokenTokenPost(
    userId: number,
    quizId: number,
    n: number = 32,
    m: number = 5
  ): CancelablePromise<any> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/token",
      query: {
        user_id: userId,
        quiz_id: quizId,
        n: n,
        m: m,
      },
      errors: {
        422: `Validation Error`,
      },
    });
  }
}
