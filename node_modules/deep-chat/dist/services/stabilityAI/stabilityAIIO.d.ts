import { KeyVerificationDetails } from '../../types/keyVerificationDetails';
import { DirectServiceIO } from '../utils/directServiceIO';
import { BuildHeadersFunc } from '../../types/headers';
import { ServiceFileTypes } from '../serviceIO';
import { APIKey } from '../../types/APIKey';
import { DeepChat } from '../../deepChat';
export declare class StabilityAIIO extends DirectServiceIO {
    insertKeyPlaceholderText: string;
    keyHelpUrl: string;
    permittedErrorPrefixes: string[];
    constructor(deepChat: DeepChat, keyVerificationDetails: KeyVerificationDetails, buildHeadersFunc: BuildHeadersFunc, apiKey?: APIKey, existingFileTypes?: ServiceFileTypes);
}
//# sourceMappingURL=stabilityAIIO.d.ts.map