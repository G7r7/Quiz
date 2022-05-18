/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Quiz } from '../models/Quiz';
import type { QuizCreate } from '../models/QuizCreate';
import type { User } from '../models/User';
import type { UserCreate } from '../models/UserCreate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Create User
     * @param requestBody 
     * @returns User Successful Response
     * @throws ApiError
     */
    public static createUserUsersPost(
requestBody: UserCreate,
): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/',
            body: requestBody,
            mediaType: 'application/json',
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
limit: number = 100,
): CancelablePromise<Array<User>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/users/list',
            query: {
                'skip': skip,
                'limit': limit,
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
userId: number,
): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/users/{user_id}',
            path: {
                'user_id': userId,
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
    public static getQuizQuizQuizIdGet(
quizId: number,
): CancelablePromise<Quiz> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/quiz/{quiz_id}',
            path: {
                'quiz_id': quizId,
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
limit: number = 100,
): CancelablePromise<Array<Quiz>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/quiz/list/{user_id}',
            path: {
                'user_id': userId,
            },
            query: {
                'skip': skip,
                'limit': limit,
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
requestBody: QuizCreate,
): CancelablePromise<Quiz> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/quiz/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}