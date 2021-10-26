from torch.utils.data import Dataset
from PIL import Image


# TODO two hierarchy index,
class DataHandler(Dataset):
    def __init__(self, edge_to, edge_from, feature_vector, time_step, transform=None):
        self.edge_to = edge_to
        self.edge_from = edge_from
        self.data = feature_vector
        self.time_step = time_step
        self.transform = transform

    def __getitem__(self, item):

        edge_to = self.edge_to[item]
        edge_from = self.edge_from[item]
        edge_to = self.data[edge_to]
        edge_from = self.data[edge_from]
        if self.transform is not None:
            # TODO correct or not?
            edge_to = Image.fromarray(edge_to)
            edge_to = self.transform(edge_to)
            edge_from = Image.fromarray(edge_from)
            edge_from = self.transform(edge_from)
        return edge_to, edge_from

    def __len__(self):
        # return the number of all edges
        return len(self.edge_to)
