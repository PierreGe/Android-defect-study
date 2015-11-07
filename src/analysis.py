import callgraphanalysis
import issueanalysis

import numpy as np
import matplotlib.pyplot as plt


def main():
    #cgscore = callgraphanalysis.score()
    #issuescore = issueanalysis.score()
    print("Bonjour")
    cgscore = {'AlarmUpdateReceiver': 2, 'DirectoryChooserActivity': 32, 'FlattrTokenFetcher': 5, 'ApplicationCallbacks': 1, 'ItunesSearchFragment': 12, 'VariableSpeedDialog': 7, 'MenuItemUtils': 3, 'ItemDescriptionFragment': 32, 'UserPreferences': 9, 'EventDistributor': 1, 'DownloadRequester': 6, 'PlayerWidget': 3, 'CoverFragment': 6, 'DownloadsFragment': 7, 'DownloadLogFragment': 11, 'AudioplayerActivity': 44, 'OpmlImportBaseActivity': 5, 'ExternalMedia': 7, 'CustomEditTextPreference': 6, 'QueueFragment': 40, 'SearchFragment': 15, 'GpodnetCallbacks': 2, 'TimeDialog': 14, 'OpmlWriter': 1, 'PreferenceController': 82, 'AllEpisodesListAdapter': 14, 'ChapterListAdapter': 19, 'ItunesAdapter': 7, 'AddFeedFragment': 14, 'GpodnetPreferences': 3, 'UpdateManager': 6, 'PreferenceActivity': 8, 'FeedRemover': 5, 'PodcastApp': 3, 'DownloadService': 26, 'RunningDownloadsFragment': 5, 'HttpDownloader': 3, 'GpodnetSetHostnameDialog': 7, 'AutoFlattrPreferenceDialog': 11, 'PlaybackPreferences': 3, 'SearchListFragment': 6, 'DownloadAuthenticationActivity': 11, 'StorageErrorActivity': 5, 'PlayerWidgetService': 9, 'FlattrClickWorker': 10, 'DefaultActionButtonCallback': 9, 'OpmlExportWorker': 7, 'FastBlurTransformation': 2, 'ConfirmationDialog': 5, 'FeedMenuHandler': 3, 'DownloadLogAdapter': 13, 'DBWriter': 45, 'FeedItemUndoToken': 3, 'FeedItemlistAdapter': 13, 'OpmlFeedChooserActivity': 12, 'PlaybackController': 18, 'PlaybackService': 43, 'FlattrAuthActivity': 12, 'SPAReceiver': 3, 'GpodnetSyncService': 7, 'Downloader': 3, 'DownloadRequest': 4, 'VideoplayerActivity': 20, 'DownloadServiceCallbacks': 4, 'CompletedDownloadsFragment': 4, 'ExternalPlayerFragment': 10, 'NavListAdapter': 13, 'FeedInfoActivity': 31, 'MainActivity': 41, 'PowerConnectionReceiver': 2, 'QueueListAdapter': 14, 'FeedImage': 1, 'EpisodesApplyActionFragment': 23, 'DBTaskLoader': 1, 'DownloadedEpisodesListAdapter': 11, 'Timeline': 5, 'ItemlistFragment': 37, 'OpmlImportFromPathActivity': 11, 'AuthenticationDialog': 9, 'ItemFragment': 58, 'ConnectivityActionReceiver': 5, 'FeedUpdateReceiver': 1, 'DownloadObserver': 6, 'SearchlistAdapter': 6, 'DBTasks': 11, 'ActionButtonUtils': 3, 'TagListFragment': 16, 'DownloadRequestErrorDialogCreator': 2, 'TagListAdapter': 5, 'MoreContentListFooterUtil': 2, 'PlaybackServiceCallbacks': 1, 'GpodnetMainFragment': 5, 'NewEpisodesFragment': 5, 'OpmlImportWorker': 7, 'VideoPlayer': 1, 'OpmlBackupAgent': 5, 'UndoBarController': 8, 'NetworkUtils': 5, 'PodcastListFragment': 25, 'FeedMedia': 4, 'GpodnetTag': 2, 'PodDBAdapter': 14, 'OnlineFeedViewActivity': 20, 'MediaButtonReceiver': 5, 'APDownloadAlgorithm': 3, 'TagFragment': 2, 'DownloadlistAdapter': 10, 'GpodnetAuthenticationActivity': 32, 'ApOkHttpUrlLoader': 1, 'DefaultOnlineFeedViewActivity': 15, 'FlattrCallbacks': 4, 'MediaplayerActivity': 40, 'OpmlImportFromIntentActivity': 4, 'AllEpisodesFragment': 38, 'PlaybackHistoryFragment': 17, 'PreferenceActivityGingerbread': 8, 'FeedItemlistDescriptionAdapter': 5, 'DownloadError': 1, 'PodcastListAdapter': 6, 'OpmlFeedQueuer': 3, 'AboutActivity': 6, 'Playable': 1, 'AspectRatioVideoView': 2, 'FeedMediaSizeService': 1, 'PlaybackServiceMediaPlayer': 22, 'FlattrUtils': 10}
    issuescore = {'DirectoryChooserActivity': 7, 'DownloadLogFragment': 8, 'ShareUtils': 4, 'ItemDescriptionFragment': 8, 'UserPreferences': 18, 'DefaultActionButtonCallback': 6, 'DownloadRequester': 30, 'AudioplayerActivity': 11, 'SyndTypeUtils': 2, 'PreferencesTest': 1, 'QueueFragment': 31, 'FeedItem': 9, 'SearchFragment': 2, 'PSMPInfo': 2, 'StorageCallbacksImpl': 4, 'DBTasksTest': 10, 'PreferenceController': 1, 'FeedItemDialog': 22, 'ServiceBackedMediaPlayer': 9, 'TypeGetter': 1, 'PreferenceActivity': 63, 'FeedRemover': 1, 'NSAtom': 7, 'NSRSS20': 4, 'RunningDownloadsFragment': 4, 'HttpDownloader': 31, 'GpodnetService': 88, 'AllEpisodesFragment': 2, 'PlayerWidgetService': 1, 'FlattrClickWorker': 2, 'FeedItemMenuHandler': 8, 'PicassoProvider': 6, 'AntennapodHttpClient': 11, 'FeedMenuHandler': 8, 'DownloadLogAdapter': 2, 'DBWriter': 11, 'FeedItemlistAdapter': 5, 'OpmlFeedChooserActivity': 2, 'FlattrAuthActivity': 2, 'DownloadActivity': 4, 'GpodnetSyncService': 4, 'DownloadLogActivity': 2, 'NSITunes': 1, 'DownloadRequest': 18, 'SearchActivity': 2, 'VideoplayerActivity': 13, 'MiroGuideSearchActivity': 2, 'FeedItemStatistics': 2, 'FeedHandler': 1, 'OpmlReader': 2, 'ExternalPlayerFragment': 2, 'DBTestUtils': 2, 'NavListAdapter': 8, 'FeedInfoActivity': 8, 'MainActivity': 22, 'PowerConnectionReceiver': 1, 'DBReaderTest': 14, 'DownloadService': 105, 'EpisodesApplyActionFragment': 1, 'DragSortController': 1, 'TestFeeds': 3, 'ItemlistFragment': 19, 'OrganizeQueueActivity': 2, 'OpmlImportFromPathActivity': 10, 'ItemFragment': 2, 'FeedUpdateReceiver': 2, 'DownloadObserver': 6, 'ActionButtonUtils': 8, 'PlaybackHistoryActivity': 4, 'HttpDownloaderTest': 4, 'Feed': 19, 'NewEpisodesFragment': 7, 'ItemviewActivity': 8, 'MiroGuideConnector': 2, 'UndoBarController': 3, 'FeedlistAdapter': 1, 'FeedMedia': 10, 'SyndHandler': 3, 'PodDBAdapter': 37, 'MediaPlayer': 6, 'GpodnetAuthenticationActivity': 2, 'ApOkHttpUrlLoader': 2, 'GpodnetActivity': 2, 'DefaultOnlineFeedViewActivity': 8, 'MiroGuideChannelViewActivity': 4, 'OpmlImportFromIntentActivity': 4, 'SyndDateUtils': 7, 'PlaybackHistoryFragment': 7, 'PlaybackService': 49, 'URLCheckerTest': 6, 'AboutActivity': 1, 'FeedHandlerTest': 1, 'MiroGuideMainActivity': 2, 'FeedItemlistActivity': 6, 'MiroGuideCategoryActivity': 2, 'FeedMediaSizeService': 6, 'AddFeedActivity': 4, 'PlaybackServiceMediaPlayer': 41, 'FlattrUtils': 8}


    j = 0
    x1 = []
    x2 = []
    for key in issuescore:
        if key in cgscore:
            for k in range(issuescore[key]):
                x1.append(j)
            for k in range(cgscore[key]):
                x2.append(j)
            j+=1
            print(key + " :" +str(issuescore[key]) + "<->" + str(cgscore[key]))


    plt.hist(x1, bins=20, histtype='stepfilled', normed=True, color='b', label='Issue')
    plt.hist(x2, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Calls')
    plt.title("Gaussian/Uniform Histogram")
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print("Hello")
    main()