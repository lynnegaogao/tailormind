export interface CameraDimensions {
    width?: number;
    height?: number;
}
export type PhotoFormat = 'png' | 'jpeg';
export interface CameraFiles {
    maxNumberOfFiles?: number;
    acceptedFormats?: string;
    format?: PhotoFormat;
    dimensions?: CameraDimensions;
}
//# sourceMappingURL=camera.d.ts.map