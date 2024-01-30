import { DirectServiceIO } from '../utils/directServiceIO';
import { BuildHeadersFunc } from '../../types/headers';
import { ServiceFileTypes } from '../serviceIO';
import { APIKey } from '../../types/APIKey';
import { DeepChat } from '../../deepChat';
export declare class AzureLanguageIO extends DirectServiceIO {
    insertKeyPlaceholderText: string;
    keyHelpUrl: string;
    permittedErrorPrefixes: string[];
    constructor(deepChat: DeepChat, buildHeadersFunc: BuildHeadersFunc, endpoint: string, apiKey?: APIKey, existingFileTypes?: ServiceFileTypes);
}
//# sourceMappingURL=azureLanguageIO.d.ts.map