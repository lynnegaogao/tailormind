import { FILE_TYPES } from '../../types/fileTypes';
type ServiceFileTypes = {
    [key in FILE_TYPES]: {
        id: string;
        svgString: string;
        dropupText: string;
    };
};
export declare const FILE_TYPE_BUTTON_ICONS: ServiceFileTypes;
export {};
//# sourceMappingURL=fileTypeButtonIcons.d.ts.map