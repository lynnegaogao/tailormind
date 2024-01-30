import { GenericObject } from './object';
import { Response } from './response';
export interface RequestDetails {
    body: any;
    headers?: GenericObject<string>;
}
export type ResponseDetails = RequestDetails | {
    error: string;
};
export type RequestInterceptor = (details: RequestDetails) => ResponseDetails | Promise<ResponseDetails>;
export type ResponseInterceptor = (response: any) => Response | Promise<Response>;
//# sourceMappingURL=interceptors.d.ts.map